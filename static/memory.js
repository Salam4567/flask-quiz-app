const cards = ["مكة","المدينة","الهجرة","الكعبة","الصلاة","القرآن"];
let cardArray = [...cards, ...cards];
cardArray.sort(() => 0.5 - Math.random());

const board = document.getElementById("game-board");
let firstCard = null, secondCard = null, score = 0;

cardArray.forEach((name) => {
    const card = document.createElement("div");
    card.classList.add("card");
    card.dataset.name = name;
    card.innerText = "?";
    card.addEventListener("click", flipCard);
    board.appendChild(card);
});

function flipCard() {
    if (!firstCard) {
        firstCard = this;
        this.innerText = this.dataset.name;
    } else if (!secondCard && this !== firstCard) {
        secondCard = this;
        this.innerText = this.dataset.name;
        checkMatch();
    }
}

function checkMatch() {
    if (firstCard.dataset.name === secondCard.dataset.name) {
        score++;
        document.getElementById("score").innerText = "النقاط: " + score;
        firstCard = null;
        secondCard = null;
        addBadge();
    } else {
        setTimeout(() => {
            firstCard.innerText = "?";
            secondCard.innerText = "?";
            firstCard = null;
            secondCard = null;
        }, 800);
    }
}

function addBadge() {
    let gamesPlayed = localStorage.getItem("gamesPlayed") || 0;
    gamesPlayed++;
    localStorage.setItem("gamesPlayed", gamesPlayed);
}
