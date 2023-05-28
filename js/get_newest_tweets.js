//set interval - virker i intervaller
//kan bruges til at opdaterer, så man hele tiden kan se de nyeste tweets
//Hvordan tjekker man så hvilke tweets der er nye og hvilke der er gamle - se næste linjer 
//setInterval(get_latest_tweets, 9000) //intervallet

async function get_latest_tweets() {
    const conn = await fetch("api-get-latest-tweets", {
        method : "POST"
    })
    const data = await conn.text()
    console.log(data)

    
}