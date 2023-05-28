//Like eller unlike et tweet 1 gang per bruger
async function retweet_tweet() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target

        // Lav reqeust til vores API om at retweet det valgte tweet
        const conn = await fetch("/retweet-tweet", {
            method : "POST",
            body : new FormData(frm),
        })

        // Hent response fra API
        const data = await conn.json();
        
        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot retweet tweet");
        }
       
        // Opdater farverne på knapper og retweet ikonet
        //update_retweet_icon(data)
        location.reload()
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

function update_retweet_icon(data){
    // Definer farver for retweet
    const buttonColorClasses = ["fill-emerald-500", "text-emerald-500", "fill-gray-500", "text-gray-500"]
    
    // Hent knappen og ikonet
    const total_retweets = document.getElementById(`total_retweets_${data.tweet_id}`)
    const retweet_btn_heart = document.getElementById(`total_retweets_heart_${data.tweet_id}`)    

    // Opdater total total retweets tallet
    total_retweets.innerHTML = data.tweet_total_retweets.toString()
    
    // Fjern den gamle farve fra knap og ikon
    total_retweets.classList.remove(...buttonColorClasses)
    retweet_btn_heart.classList.remove(...buttonColorClasses)

    // Sæt farver for "not retweet" tweet 
    if ( data.retweeted == 0 ) {
        total_retweets.classList.add(buttonColorClasses[3])
        retweet_btn_heart.classList.add(buttonColorClasses[2])
        console.log("den er 0")
    } 

    // Sæt farver for retweet tweet
    total_retweets.classList.add(buttonColorClasses[1])
    retweet_btn_heart.classList.add(buttonColorClasses[0])
}