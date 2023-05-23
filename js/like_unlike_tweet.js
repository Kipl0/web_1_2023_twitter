//Like eller unlike et tweet 1 gang per bruger

async function like_tweet() {
    const frm = event.target

    const conn = await fetch("/like-tweet", {
        method : "POST",
        body : new FormData(frm),
    })
    const data = await conn.json();
    
    //Vis increase i likes i html
    if( conn.ok && data.info == "ok" ) {
        const like_unlike_btn = document.getElementById(`total_likes_${data.tweet_id}`)
        const like_unlike_heart = document.getElementById(`heart_${data.tweet_id}`)    

        const buttonColorClasses = ["fill-pink-600", "text-pink-600", "fill-gray-500", "text-gray-500"]
        
        like_unlike_btn.innerHTML = data.tweet_total_likes.toString()
        
        like_unlike_btn.classList.remove(...buttonColorClasses)
        like_unlike_heart.classList.remove(...buttonColorClasses)

        if ( data.liked_viewed == 0 ) {
            like_unlike_btn.classList.add(buttonColorClasses[3])
            like_unlike_heart.classList.add(buttonColorClasses[2])
            return
        } 

        like_unlike_btn.classList.add(buttonColorClasses[1])
        like_unlike_heart.classList.add(buttonColorClasses[0])
        return
    }
    else {
        //noget gik galt i API conn
        console.log("conn", conn.ok)

        console.log("cannot like tweet")
    }
}
