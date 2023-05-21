// --------------------------------------
//        ÅBN pop up - kun read
// --------------------------------------

async function write_tweet_pop_up() {
    const frm = event.target

    const form_data = new FormData(frm)
    
    // Det her er det samme som "request.forms.get("tweet_id")" i python.
    // Vi gør dette da et GET request ikke må have en body, som er der hvor vi normalt sender form_data til python
    // Vi er nødt til at have en body med da vi skal finde ud af hvilken tweet vi har klikket på 
    const tweet_id = form_data.get("tweet_id");
    
    const conn = await fetch(`/write-tweet-comment-pop-up/${tweet_id}`, {
        method : "GET"  // id bliver passet ind til python instedet for hele formen
    })     

    const data = await conn.json()
    const tweets_and_user_data_data = JSON.parse(data.tweets_and_user_data);


    if( conn.ok && data.info == "ok" ) {
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

        const write_tweet_form_container = document.getElementById("write_tweet_form_container")
        // Open close
        if(write_tweet_form_container.classList.contains("hidden")) {
            write_tweet_form_container.classList.remove("hidden")
            write_tweet_form_container.classList.add("flex")
        } else {
            write_tweet_form_container.classList.add("hidden")
            write_tweet_form_container.classList.remove("flex")
        }

    } else {
        console.log("cannot write comment")
    }
}

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



// --------------------------------------
//        Skriv og send komment
// --------------------------------------
async function write_tweet_comment() {
    const frm = event.target

    const conn = await fetch("/write-tweet-comment", {
        method : "POST",
        body : new FormData(frm)
    })

    const data = await conn.json()

    if(conn.ok && data.info == "ok") {
        console.log("tester ok")

    } else {
        console.log("nope")
    }
}