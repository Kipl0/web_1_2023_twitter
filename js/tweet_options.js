// Definer globale variabler
let active_popup = null;
let tweet_options_btn_g 
let tweet_option_popup

/**
 * Denne funktion bliver kaldt en gang når js filen bliver importeret
 * - Formålet med dette er at lave kun en eventlistener.
 */
function init() {
    // Close popup when clicked outside button and popup
    document.addEventListener("click", (e) => {
         if (active_popup && e.target !== active_popup.button && !active_popup.popup.contains(e.target)  && !active_popup.button.contains(e.target)) {
            active_popup.popup.classList.remove("flex");
            active_popup.popup.classList.add("hidden");
            active_popup = null
        } 
    });
}

// Kald når js filen bliver importeret
init()

/**
 * Åbn & Luk pop up til logud i navbar
 * @param {object} data - Data som inderholder tweet informationer.
 */
function tweet_options_popup(tweet_options_btn) {
    tweet_options_btn_g = tweet_options_btn
    const tweet_option_popup_text = "tweet_option_popup"
    
    // Split the text from the id where _
    const parts = tweet_options_btn.id.split("_");
    const id = parts[parts.length - 1];
    const retweet_identifyer = parts[parts.length - 2]

    const tweet_option_popup_and_id = tweet_option_popup_text + "_" + retweet_identifyer + "_" + id;
    console.log(tweet_option_popup_and_id)
    tweet_option_popup = document.getElementById(tweet_option_popup_and_id);

    // Show and hide popup
    if (active_popup && active_popup.popup !== tweet_option_popup) {
        active_popup.popup.classList.remove("flex");
        active_popup.popup.classList.add("hidden");
        active_popup = null;
    }

    // Toggle the visibility of the popup
    if (tweet_option_popup.classList.contains("hidden")) {
        tweet_option_popup.classList.remove("hidden");
        tweet_option_popup.classList.add("flex");
        active_popup = { button: tweet_options_btn, popup: tweet_option_popup };
    } else {
        tweet_option_popup.classList.remove("flex");
        tweet_option_popup.classList.add("hidden");
        active_popup = null;
    }
}


/**
 * Delete tweet from database
 */
async function delete_tweet(){
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target

        // Lav reqeust til vores API om at delete tweet
        const conn = await fetch("/delete-tweet", {
            method : "DELETE",
            body : new FormData(frm),        
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot like tweet");
        }
    
        const testertester = document.getElementById(`${data.tweet_to_delete_id}`)
        testertester.style.display="none"
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

