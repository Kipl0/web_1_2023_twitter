/**
 * Check om brugeren findes i databasen og send derefter en sms med verification numre
 */
async function check_user_exists_and_send_sms() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target   
        const frmData = new FormData(frm)

        // Lav reqeust til vores API om at write tweet comment for det valgte tweet
        const conn = await fetch("/twitter-gold", {
            method : "POST",
            body : frmData
        })

        // Hent response fra API
        const data = await conn.json()
        
        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot like tweet");
        }
        
        const sms_message = "Your verification numbers are : " + data.sms_confirm_digits

        const get_twitter_gold_form = document.getElementById("get_twitter_gold_form")
        const confirm_digits_form = document.getElementById("confirm_digits_form")

        get_twitter_gold_form.classList.remove("flex")
        get_twitter_gold_form.classList.add("hidden")

        confirm_digits_form.classList.add("flex")
        confirm_digits_form.classList.remove("hidden")
        
        send_sms(sms_message, frmData.get("twitter_gold_phone"))
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}

/**
 * Send sms til brugeren
 * @param {string} sms_message - Inderholder sms beskeden.
 * @param {string} sms_to_phone - Inderholder telefon nummeret.
 */
async function send_sms(sms_message, sms_to_phone) {
    // Opret top FormData object
    let bodyContent = new FormData();

    // Tilføj data til FormData object
    bodyContent.append("user_api_key", "c091d82de07d0413b9c0d6aa575c6123");
    bodyContent.append("sms_message", sms_message);
    bodyContent.append("sms_to_phone", sms_to_phone);

    // Lav reqeust til fiotext API om at sende sms'en
    let response = await fetch("https://fiotext.com/send-sms", { 
        method: "POST",
        body: bodyContent,
    });

    // Hent response fra API
    let data = await response.text();
    console.log(data);
}

/**
 * Bekræft twitter gold status
 */
async function confirm_twitter_gold() {
    try {    
        // Hent event target som i vores tilfælde er en form
        const frm = event.target   

        // Lav reqeust til vores API om at confirm twitter gold
        const conn = await fetch("/confirm-twitter-gold", {
            method: "POST",
            body : new FormData(frm)
        })

        // Hent response fra API
        const data = await conn.json()

        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            twitter_gold_tip.innerHTML = "Something went wrong, please try again"
            throw new TypeError("Something went wrong");
        }
        

        const twitter_gold_tip = document.getElementById("twitter_gold_tip")
        const confirm_digits_form = document.getElementById("confirm_digits_form")

        confirm_digits_form.classList.remove("flex")
        confirm_digits_form.classList.add("hidden")

        twitter_gold_tip.innerHTML = "Cheers! You upgraded to twitter gold!"
    } 
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}