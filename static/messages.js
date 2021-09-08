const Form = document.querySelector(".msger-inputarea");
const Input = document.querySelector(".msger-input");
const Chat = document.querySelector(".msger-chat");


const BOT_IMG = "https://image.flaticon.com/icons/svg/327/327779.svg";
const PERSON_IMG = "https://image.flaticon.com/icons/svg/145/145867.svg";
const BOT_NAME = "SARSBot";
const PERSON_NAME = "You";

Form.addEventListener("submit", event => {
    event.preventDefault();

    const msgText = Input.value;
    if (!msgText) return;

    appendMessage(PERSON_NAME, PERSON_IMG, "right", msgText);
    Input.value = "";
    botResponse(msgText);
});

function appendMessage(name, img, side, text) {
    const msgHTML = `
<div class="msg ${side}-msg">
  <div class="msg-img" style="background-image: url(${img})"></div>
  <div class="msg-bubble">
    <div class="msg-info">
      <div class="msg-info-name">${name}</div>
      <div class="msg-info-time">${formatDate(new Date())}</div>
    </div>
    <div class="msg-text">${text}</div>
  </div>
</div>
`;

    Chat.insertAdjacentHTML("beforeend", msgHTML);
    Chat.scrollTop += 500;
}

function botResponse(rawText) {

    // Bot Response
    $.get("/get", {msg: rawText}).done(function (data) {
        console.log(rawText);
        console.log(data);
        const msgText = data;
        appendMessage(BOT_NAME, BOT_IMG, "left", msgText);

    });

}

function formatDate(date) {
    const h = "0" + date.getHours();
    const m = "0" + date.getMinutes();

    return `${h.slice(-2)}:${m.slice(-2)}`;
}
