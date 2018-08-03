<strong>Steamsnitch</strong> is a script written in python to estimate the approximate value of a steam account. The script is very slow at this point and it will take several minutes to complete the process, in other words more games will need more time. <br><br>
It consists of a class with 3 methods : <br>
<ul>
 <li>ResolveVanityURL - Converts the custom URL to SteamID</li>
 <li>GetOwnedGames - Creates a list with all the appIDs that belong to the account</li>
 <li>AccInfo - Checks every game in the above list for their price and it's been added to the counter</li>
</ul><br><br>
To use it you need to create an object of the class EstimateValue and pass the API_KEY along with the custom URL<strong>(example: x = EstimateValue('your_api_key', 'custom_url') )</strong> and then call the method AccInfo on the object x<strong>(example: x.AccInfo()</strong><br><br><br>

<strong>NOTICE: </strong> You need a valid API key and the custom URL for the account you want to estimate it's value
<strong>NOTICE: </strong> The script won't estimate the value based on the price you bought the game but with the normal price of the game at this given time, also it won't add the price of your DLCs into the total value
