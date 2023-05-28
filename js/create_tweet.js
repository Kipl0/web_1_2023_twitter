// Create tweet

async function tweet() {
    
    const frm = event.target.form;
    const conn = await fetch("/tweet", {
        method: "POST",
        body: new FormData(frm)
    });

    const data = await conn.json();
    console.log(data)
    if (!conn.ok) {
        const errorTip = document.getElementById("error-tip");
        errorTip.innerText = data.error; // Assuming the server returns an 'error' field in the response
        errorTip.style.display = "block";
        console.log(data.error)
        return;
    }


  



    location.reload();
}

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
