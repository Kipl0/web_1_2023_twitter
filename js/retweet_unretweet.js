//Like eller unlike et tweet 1 gang per bruger

async function retweet_tweet() {
    const frm = event.target

    const conn = await fetch("/retweet-tweet", {
        method : "POST",
        body : new FormData(frm),
    })
    const data = await conn.json();
    
    console.log(data)
    //Vis increase i likes i html
    if( conn.ok && data.info == "ok" ) {
        const total_retweets = document.getElementById(`total_retweets_${data.tweet_id}`)
        const retweet_btn_heart = document.getElementById(`total_retweets_heart_${data.tweet_id}`)    

        const buttonColorClasses = ["fill-emerald-500", "text-emerald-500", "fill-gray-500", "text-gray-500"]
        
        total_retweets.innerHTML = data.tweet_total_retweets.toString()
        
        total_retweets.classList.remove(...buttonColorClasses)
        retweet_btn_heart.classList.remove(...buttonColorClasses)

        if ( data.retweeted == 0 ) {
            total_retweets.classList.add(buttonColorClasses[3])
            retweet_btn_heart.classList.add(buttonColorClasses[2])
            console.log("den er 0")
            // return
        } 

        total_retweets.classList.add(buttonColorClasses[1])
        retweet_btn_heart.classList.add(buttonColorClasses[0])
        return
    }


    else {
        //noget gik galt i API conn
        console.log("conn", conn.ok)

        console.log("cannot like tweet")
    }

}
