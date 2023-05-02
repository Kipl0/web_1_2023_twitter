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
        console.log("data", data)
        const total_likes_element = document.getElementById(`${data.tweet_id}`)

        total_likes_element.innerHTML = data.tweet_total_likes.toString()

        let like_unlike_btn = document.getElementById(`${data.tweet_id}`)    
        let like_unline_heart = document.getElementById(`heart_${data.tweet_id}`)   

        const buttonColorClasses = ["fill-pink-600", "text-pink-600", "fill-gray-500", "text-gray-500"]
        like_unlike_btn.classList.remove(...buttonColorClasses)
        like_unline_heart.classList.remove(...buttonColorClasses)

        if ( data.liked == 0 ) {
            like_unlike_btn.classList.add(buttonColorClasses[3])
            like_unline_heart.classList.add(buttonColorClasses[2])
        } else {
            like_unlike_btn.classList.add(buttonColorClasses[1])
            like_unline_heart.classList.add(buttonColorClasses[0])
        }

        return
    }



    //noget gik galt i API conn
    console.log("conn", conn.ok)

    console.log("cannot like tweet")
}
