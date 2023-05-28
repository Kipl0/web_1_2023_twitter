async function check_user_exists_and_send_sms() {
    const frm = event.target   
    const frmData = new FormData(frm)
    const conn = await fetch("/twitter-gold", {
        method : "POST",
        body : frmData
    })
    const data = await conn.json()

    if(conn.ok && data.info == "ok") {
        const sms_message = "Your verification numbers are : " + data.sms_confirm_digits

        // const get_twitter_gold_form = document.getElementById("get_twitter_gold_form")
        // const confirm_digits_form = document.getElementById("confirm_digits_form")

        // get_twitter_gold_form.classList.remove("flex")
        // get_twitter_gold_form.classList.add("hidden")

        // confirm_digits_form.classList.add("flex")
        // confirm_digits_form.classList.remove("hidden")
        
        send_sms(sms_message, frmData.get("twitter_gold_phone"))
    } else {
        console.log("nope")
    }
}


async function send_sms(sms_message, sms_to_phone) {
    let bodyContent = new FormData();

    bodyContent.append("user_api_key", "c091d82de07d0413b9c0d6aa575c6123");
    bodyContent.append("sms_message", sms_message);
    bodyContent.append("sms_to_phone", sms_to_phone);

    let response = await fetch("https://fiotext.com/send-sms", { 
        method: "POST",
        body: bodyContent,
    });

    let data = await response.text();
    console.log(data);

}

async function confirm_twitter_gold() {
    const frm = event.target   
    const conn = await fetch("/confirm-twitter-gold", {
        method: "POST",
        body : new FormData(frm)
    })

    const data = await conn.json()

    if(conn.ok && data.info == "ok") {
        const get_twitter_gold_form = document.getElementById("get_twitter_gold_form")
        const twitter_gold_tip = document.getElementById("twitter_gold_tip")

        confirm_digits_form.classList.remove("flex")
        confirm_digits_form.classList.add("hidden")

        twitter_gold_tip.innerHTML = "Cheers! You upgraded to twitter gold!"
    } else {
        twitter_gold_tip.innerHTML = "Something went wrong, please try again"
        console.log("nope")
    }
}