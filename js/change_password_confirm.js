async function change_password_confirm() {

    url = window.location.href
    url_split = url.split("/")

    user_key = url_split[url_split.length - 1] //få det sidste element fra array

    const frm = event.target
    const conn = await fetch(`/confirm-new-password/${user_key}`, {
        method: "POST",
        body: new FormData(frm)
    })
    const data = await conn.json()
    console.log(data)

    if(conn.ok && data.info == "ok") {
        console.log("ok")
        // redirect to login
        location.href = `/login`
    } else {
        console.log("data ikke ok")
    }
}