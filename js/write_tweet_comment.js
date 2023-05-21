
async function write_tweet_pop_up() {
    const frm = event.target
    const conn = await fetch("/write-tweet-comment", {
        method : "POST",
        body : new FormData(frm),  // id bliver passet ind til python instedet for hele formen
    })     

    const data = await conn.json()
    const tweets_and_user_data_data = JSON.parse(data.tweets_and_user_data);

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




    // if( conn.ok && data.info == "ok" ) {
    //     console.log(data)

    // } else {
    //     console.log("cannot write comment")
    // }
    const write_tweet_form_container = document.getElementById("write_tweet_form_container")

    if(write_tweet_form_container.classList.contains("hidden")) {
        write_tweet_form_container.classList.add("flex")
        write_tweet_form_container.classList.remove("hidden")
    } 

}