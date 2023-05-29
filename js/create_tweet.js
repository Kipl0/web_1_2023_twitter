/**
 * Create a new tweet
 */
async function tweet() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target.form;

        // Lav reqeust til vores API om at create new tweet
        const conn = await fetch("/tweet", {
            method: "POST",
            body: new FormData(frm)
        });

        // Hent response fra API
        const data = await conn.json();
        
        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            const errorTip = document.getElementById("error-tip");
            errorTip.innerText = data.error; //Vi antager at serveren retunere et 'error' field i responset
            errorTip.style.display = "block";
            
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }

        // Reload siden
        location.reload();
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

/**
 * Denne funktion bliver kaldt en gang når js filen bliver importeret
 * - Formålet med dette er at lave kun en eventlistener.
 */
function init() {
    let uploaded_create_tweet_img = "";
    const uploaded_create_tweet_img_input = document.getElementById("uploaded_create_tweet_img_input");

    uploaded_create_tweet_img_input.addEventListener("change", function() {
        const reader = new FileReader();
        reader.addEventListener("load", () => {
            uploaded_create_tweet_img = reader.result;
            document.getElementById("uploaded_create_tweet_img").src = uploaded_create_tweet_img;
        });
        reader.readAsDataURL(this.files[0]);
    });
}

// Kald init når js filen bliver importeret
init()

