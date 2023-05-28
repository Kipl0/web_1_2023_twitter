// Like eller unlike et tweet 1 gang per bruger
async function like_tweet() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target

        // Lav reqeust til vores API om at like det valgte tweet
        const conn = await fetch("/like-tweet", {
            method : "POST",
            body : new FormData(frm),
        })

        // Hent response fra API
        const data = await conn.json();

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot like tweet");
        }

        // Opdater farverne på knapper og hjerte ikonet, samt total likes værdien
        update_like_icon(data)
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

function update_like_icon(data){
    // Definer farver for like og unlike 
    const buttonColorClasses = ["fill-pink-600", "text-pink-600", "fill-gray-500", "text-gray-500"]
    
    // Hent like knappen og hjerte ikonet (Select all i tilfældet af et retweet)
    const like_unlike_btns = document.querySelectorAll(`[id=total_likes_${data.tweet_id}]`);
    const like_unlike_hearts = document.querySelectorAll(`[id=heart_${data.tweet_id}]`);  

    // Loop igennem alle iconer og knapper (Igen, det er i tilfældet af et rewteet)
    for(let i=0; i<like_unlike_btns.length; i++){
        // Opdater total likes tallet
        like_unlike_btns[i].innerHTML = data.tweet_total_likes.toString()
    
        // Fjern den gamle farve fra knap og ikon
        like_unlike_btns[i].classList.remove(...buttonColorClasses)
        like_unlike_hearts[i].classList.remove(...buttonColorClasses)

        // Sæt farver for "not liked" tweet 
        if ( data.liked == 0 ) {
            like_unlike_btns[i].classList.add(buttonColorClasses[3])
            like_unlike_hearts[i].classList.add(buttonColorClasses[2])
            
            // Hop videre i for lykke, da vi ikke ønsker næste del bliver eksekveret
            continue
        } 

        // Sæt farver for liked tweet
        like_unlike_btns[i].classList.add(buttonColorClasses[1])
        like_unlike_hearts[i].classList.add(buttonColorClasses[0])
    }
}