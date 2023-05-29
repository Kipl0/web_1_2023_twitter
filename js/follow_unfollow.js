/**
 * Follow or unfollow a user
 */
async function follow_unfollow() {
    try {
        // Hent event target som i vores tilfælde er en form
        const frm = event.target

        // Lav reqeust til vores API om at follow-unfollow
        const conn = await fetch("/follow-unfollow", {
            method : "POST",
            body : new FormData(frm),
        })

        // Hent response fra API
        const data = await conn.json();


        // Tjek om requestet gik igennem og kast en error hvis ikke det skete
        if( !conn.ok || data.info != "ok" ) {
            throw new TypeError("Something went wrong. Cannot write comment to tweet");
        }
        
        
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
    catch ({ name, message }) {
        console.log(name); 
        console.log(message); 
    }
}
