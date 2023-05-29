/**
 * ÅBN pop up - kun read
 */
async function write_tweet_pop_up() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target

        // Det her er det samme som "request.forms.get("tweet_id")" i python.
        // Vi gør dette da et GET request ikke må have en body, som er der hvor vi normalt sender form_data til python
        // Vi er nødt til at have en body med da vi skal finde ud af hvilken tweet vi har klikket på 
        const form_data = new FormData(frm)
        const tweet_id = form_data.get("tweet_id");

        // Lav reqeust til vores API om at get tweet comment for det valgte tweet
        // - id bliver passet ind til python instedet for hele formen
        const conn = await fetch(`/write-tweet-comment-pop-up/${tweet_id}`, {
            method : "GET"  
        })     

        // Hent response fra API
        const data = await conn.json()
        const tweets_and_user_data_data = JSON.parse(data.tweets_and_user_data);

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }

        update_comment_pop_up_form(tweet_id, tweets_and_user_data_data)
        open_close_comment_container();

    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

/**
 * Skriv og send komment
 * @param {boolean} show_pop_up - Indikere om popup elementet skal vises eller ej.
 */
async function write_tweet_comment(show_pop_up) {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target
        const frmData = new FormData(frm)
       
        // Lav reqeust til vores API om at write tweet comment for det valgte tweet
        const conn = await fetch("/write-tweet-comment", {
            method : "POST",
            body : frmData
        })

        // Hent response fra API
        const data = await conn.json()

        if(conn.ok && data.info == "no data"){
            const infoText = document.getElementById("infoText")
            infoText.innerHTML = "You need write something or add an image"
            infoText.classList.remove("hidden")
        }

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }

        if(show_pop_up == true) {
            update_comment_icon(data)
            open_close_comment_container()
        }
        else {
            // Reload siden
            location.reload()
        }
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}


// --------------------------------------
//        Hjælper funktioner
// --------------------------------------

/**
 * Opdater kommentar popup elementet
 * @param {string} tweet_id - Indeholder et id for et tweet.
 * @param {object} tweets_and_user_data_data - Inderholder for tweets samt de bruger der oprettet dem.
 */
function update_comment_pop_up_form(tweet_id, tweets_and_user_data_data){
    const tweet_comment_textarea = document.getElementById("tweet_comment_textarea")
    tweet_comment_textarea.value = ""
    // Formen for at brugeren kan skrive sin kommentar har brug for tweet_id - her sættes det input felt der sidder i den form til tweet-id value
    const tweet_id_to_html = document.getElementById("tweet_id_to_html")
    tweet_id_to_html.value = tweet_id

    // Man kan ikke returnere en dictionary i en dictionary som json (den hentes som json i js) - derfor bruges json.dumps i python og parse herinde
    const comment_tweet_avatar = document.getElementById("comment_tweet_avatar")
    comment_tweet_avatar.src = `/avatar/${tweets_and_user_data_data.user_avatar}`

    const comment_tweet_first_name = document.getElementById("comment_tweet_first_name")
    comment_tweet_first_name.innerHTML = `${tweets_and_user_data_data.user_last_name}`

    const comment_tweet_last_name = document.getElementById("comment_tweet_last_name")
    comment_tweet_last_name.innerHTML = `${tweets_and_user_data_data.user_first_name}`


    const comment_tweet_username = document.getElementById("comment_tweet_username")
    comment_tweet_username.innerHTML = `${tweets_and_user_data_data.user_username}`

    if(tweets_and_user_data_data.tweet_message != "") {
        const comment_tweet_message = document.getElementById("comment_tweet_message")
        comment_tweet_message.innerHTML = `${tweets_and_user_data_data.tweet_message}`
    } else {
        comment_tweet_message.innerHTML = ""
    }

    if(tweets_and_user_data_data.tweet_image != "") {
        const comment_tweet_image = document.getElementById("comment_tweet_image")
        comment_tweet_image.src = `/tweet_images/${tweets_and_user_data_data.tweet_image}`
    }


    // Hvis brugeren ønsker at lave kommentar med billede
    let uploaded_comment_img = "";
    const uploaded_comment_img_input = document.getElementById("uploaded_comment_img_input");

    uploaded_comment_img_input.addEventListener("change", function() {
        const reader = new FileReader();
        reader.addEventListener("load", () => {
            uploaded_comment_img = reader.result;
            document.getElementById("uploaded_comment_img").src = uploaded_comment_img;
        });
        reader.readAsDataURL(this.files[0]);
    });

}

/**
 * Skriv og send komment
 * @param {object} data - Indeholder data for comment tweet.
 */
function update_comment_icon(data){
    // Definer farver for like og unlike 
     const buttonColorClasses = ["fill-[#1D9BF0]", "text-[#1D9BF0]", "fill-gray-500", "text-gray-500"] 
    
    // Hent comment knappen og  ikonet (Select all i tilfældet af et retweet)
    const total_comments_btns = document.querySelectorAll(`[id=total_comments_btn_${data.tweet_id}]`)
    const total_comments_icons = document.querySelectorAll(`[id=total_comments_icon_${data.tweet_id}]`)    

    // Loop igennem alle iconer og knapper (Igen, det er i tilfældet af et rewteet)
    for(let i=0; i<total_comments_btns.length; i++){
        total_comments_btns[i].innerHTML = data.tweet_total_comments.toString()
        
        total_comments_btns[i].classList.remove(...buttonColorClasses)
        total_comments_icons[i].classList.remove(...buttonColorClasses)


        total_comments_btns[i].classList.add(buttonColorClasses[1])
        total_comments_icons[i].classList.add(buttonColorClasses[0])
    }
}

/**
 * Skriv og send komment
 * @param {Event} event - event der kommer fra en onClick funtion i html.
 */
function closeOverlay(event) {
    // Skal bruges til at tjekke, om bruger klikker på div hvor id sidder på eller på svg, path og span der sidder inde i den div contains(event.target)
    const close_tweet_x = document.getElementById("close_tweet_x")

    if (event.target.id === "write_tweet_form_container" || event.target.id == close_tweet_x || close_tweet_x.contains(event.target) ) {
        // åbn/luk overlay og pop up
        let write_tweet_form_container = document.getElementById("write_tweet_form_container");
        write_tweet_form_container.classList.add("hidden")
        write_tweet_form_container.classList.remove("flex")
    }
}

/**
 * Åben & Luk kommentar kontainer
 */
function open_close_comment_container(){
     const write_tweet_form_container = document.getElementById("write_tweet_form_container")
    // Open close
    if(write_tweet_form_container.classList.contains("hidden")) {
        write_tweet_form_container.classList.remove("hidden")
        write_tweet_form_container.classList.add("flex")
    } else {
        write_tweet_form_container.classList.add("hidden")
        write_tweet_form_container.classList.remove("flex")
    }
}