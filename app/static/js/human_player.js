let currentSlot = 1;

// Fonction pour changer la couleur de la case
function changeColor(color) {
    const slot = document.getElementById("slot" + currentSlot);
    slot.style.backgroundColor = color;
    document.getElementById("combination").value = getCombination();
}

// Fonction pour récupérer la combinaison actuelle en premières lettres des couleurs en français
function getCombination() {
    let combination = '';
    const colorToLetter = {
        'red': 'R',    // Rouge
        'blue': 'B',   // Bleu
        'green': 'V',  // Vert
        'yellow': 'J', // Jaune
        'black': 'N',  // Noir
        'grey': 'G',
        'black': 'N',
        'orange': 'O',
        'brown': 'M',
    };

    for (let i = 1; i <= 4; i++) {
        const slot = document.getElementById("slot" + i);

        for (let colorKey in colorToLetter) {
            if (slot.style.backgroundColor === colorKey) {
                combination += colorToLetter[colorKey] + "";
                console.log(combination)
                break;
            }
        }
    }
    return combination.trim();
}

// Permet de changer de slot en cliquant sur la plaque
document.querySelectorAll('.slot').forEach(function (slot) {
    slot.addEventListener('click', function () {
        currentSlot = parseInt(slot.id.replace('slot', ''));
    });
});