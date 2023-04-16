// Create tweet

async function tweet() {
    const frm = event.target.form //the event is where - target is the form
    const conn = await fetch("/tweet", {
        method: "POST",
        body: new FormData(frm)
    })
    console.log(conn)
    // TODO: show tip
    // const data = await conn.text()
    // console.log(data)
    // const message = frm.querySelector("input[name='message']").value
    // console.log(message)
    if( !conn.ok ){
        console.log("cannot tweet")
        // showTip()        
        return
    }
    location.reload()
}