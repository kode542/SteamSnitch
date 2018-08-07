import requests



class EstimateValue:
    
    game_count = 0
    
    # Constructor requires API Key and User Profile URL(User's Vanity URL)
    def __init__(self, key, url):
        self.API_KEY = key
        self.SP_URL = url
        
    # Finds and returns SteamID
    def ResolveVanityURL(self):
        # SteamID from Custom Profile URL
        response = requests.get('http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=' + self.API_KEY + '&vanityurl=' + self.SP_URL)
        # SteamID
        steamid = response.json()['response']['steamid']
        return steamid
    
    # Get appIDs of owned games
    def GetOwnedGames(self):
        # SteamID
        self.SteamID = self.ResolveVanityURL()
        # Get AppIDs
        response = requests.get('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key='+ self.API_KEY +'&steamid=' + self.SteamID + '&format=json')
        # JSON
        gamesList = response.json()['response']['games']
        # Create Games List with List Comprehension
        games = [i['appid'] for i in gamesList]
        return games
        
    def AccInfo(self):
        # Get Owned Games list through the method GetOwnedGames() and save it to Games
        self.GamesList = self.GetOwnedGames()
        # Account
        account_total = 0
        free = 0
        paid = 0
        wrongid = 0
        i = 0
        game_count = len(self.GetOwnedGames())
        # Iterate through Games List
        for Game in self.GamesList:
            
            
            
            # Get request to obtain app(game) details
            response = requests.get('http://store.steampowered.com/api/appdetails?appids=' + str(Game))
            
            
            # success state can take boolean values
            success = response.json()[str(Game)]['success']
            
            # If success == True
            if(success):
                # is_free state can take boolean values
                is_free = response.json()[str(Game)]['data']['is_free']
                # If game is free add 1 to free variable
                if(is_free):
                    free += 1
                    
                # If game is not free
                elif(is_free == False):
                    
                    # Check if key 'price_overview' exists in 'data'
                    if('price_overview' in response.json()[str(Game)]['data']):
                        price = response.json()[str(Game)]['data']['price_overview']['initial']
                        # Add the current game's price into account_value
                        account_total += int(price)
                        paid += 1
                    # Check if key 'package_groups' exists in JSON and that package_groups isn't an empty list 
                    elif('package_groups' in response.json()[str(Game)]['data'] and not response.json()[str(Game)]['data']['package_groups'] == []):
                        package_groups = response.json()[str(Game)]['data']['package_groups'][0]
                        # Add the current game's package price into account_value
                        account_total += int(package_groups['subs'][0]['price_in_cents_with_discount'])
                        paid += 1
                    # Anything else would be experimental or test server app
                    else:
                        free += 1
                        
            # If success == False        
            else:
                wrongid += 1
            
            i += 1
            print('\r', 'Checked ', i, ' out of ', game_count, ' games', end='')
            
        # Convert amount from cents to euro    
        total_amount = account_total / 100 
        # Print info
        print('\nApprox. value from the games in your account :  ' , total_amount, ' €\n')
        print('You have : ', free, 'free games')
        print('\t   ' , paid, 'paid games')
        print('\nWrong or Missing AppIDs :', wrongid)
        
# Create an object of the class EstimateValue with two params EstimateValue('Api_key', 'VanityURL')
x = EstimateValue('', '')
# Call the method AccInfo() on the object x
x.AccInfo()



