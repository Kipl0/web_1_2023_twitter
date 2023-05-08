async function follow_unfollow() {
    const frm = event.target

    const conn = await fetch("/follow-unfollow", {
        method : "POST",
        body : new FormData(frm),
    })
    const data = await conn.json();

    if(conn.ok && data.info == "ok") {
        const total_followers_element = document.getElementById(`${data.user_id}`)
        total_followers_element.innerHTML = data.user_total_followers.toString()

        let follow_unfollow_btn = document.getElementById(`follow_btn_${data.user_id}`)
        if(data.follows == 1) {
            follow_unfollow_btn.style.backgroundColor = "black"
            follow_unfollow_btn.style.border = "2px solid white"
            follow_unfollow_btn.style.color = "white"
            follow_unfollow_btn.innerHTML = "Unfollow"
        } else {
            follow_unfollow_btn.style.backgroundColor = "white"
            follow_unfollow_btn.style.color = "black"
            follow_unfollow_btn.innerHTML = "Follow"
        }

    }
    else {
        console.log("cannot follow user")
    }

}
