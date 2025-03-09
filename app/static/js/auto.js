// Vérifie que le script est chargé
console.log("auto.js chargé !");

// Vérifie que la variable attempts est bien définie
console.log("attempts:", attempts);

// Variables globales
let currentAttempt = 1;
let totalAttempts = attempts.length;
const letterToColor = {
    'R': 'red',    // Rouge
    'B': 'blue',   // Bleu
    'V': 'green',  // Vert
    'J': 'yellow', // Jaune
    'N': 'black',  // Noir
    'G': 'grey',   // Gris
    'O': 'orange', // Orange
    'M': 'brown',  // Marron
};

// Fonction pour mettre à jour les evaluation-slot
function updateEvaluationSlots(line, cplaced, iplaced) {
    let slots = document.querySelectorAll(`.evaluation-area-${line} .evaluation-slot`);
    
    if (!slots.length) {
        console.warn(`Aucun slot trouvé pour la ligne ${line}`);
        return;
    }

    let index = 0;

    for (let i = 0; i < cplaced; i++) {
        if (index < slots.length) {
            slots[index].style.backgroundColor = "red";
            localStorage.setItem(`evaluation-slot-${line}-${index}`, "red");
            index++;
        }
    }

    for (let i = 0; i < iplaced; i++) {
        if (index < slots.length) {
            slots[index].style.backgroundColor = "white";
            localStorage.setItem(`evaluation-slot-${line}-${index}`, "white");
            index++;
        }
    }
}

// Fonction pour afficher les tentatives successives
function displayNextAttempt() {
    console.log("displayNextAttempt appelée, currentAttempt:", currentAttempt);

    // Vérifier que nous avons encore des tentatives à traiter
    if (currentAttempt < totalAttempts) {
        // Récupérer l'essai actuel de la liste `attempts`
        let attemptStr = attempts[currentAttempt];
        console.log("Traitement de l'essai:", attemptStr);

        // Vérifier que la structure de l'essai correspond au format attendu
        let match = attemptStr.match(/Essai (\d+) : ([A-Z]+) \((\d+) bien placées, (\d+) mal placées\)/);

        if (match) {
            console.log("Regex matchée:", match);

            let attemptNum = parseInt(match[1]);  // Numéro de l'essai
            let combination = match[2];          // Combinaison testée
            let cplaced = parseInt(match[3]);    // Nombre de bien placés
            let iplaced = parseInt(match[4]);    // Nombre de mal placés

            // Mettre à jour les plots avec les couleurs de la combinaison testée
            for (let i = 0; i < combination.length; i++) {
                let slot = document.getElementById(`slot-${currentAttempt}-${i + 1}`);
                if (slot) {
                    console.log(`Mise à jour du slot ${i + 1} avec la couleur`, combination[i]);
                    slot.style.backgroundColor = letterToColor[combination[i]];
                } else {
                    console.warn(`Slot slot-${currentAttempt}-${i + 1} introuvable`);
                }
            }

            // Mettre à jour les slots d'évaluation
            updateEvaluationSlots(currentAttempt, cplaced, iplaced);

            // Mettre à jour la position de la flèche
            const arrow = document.querySelector(".arrow-container");
            if (arrow) {
                const lineHeight = 55; // Hauteur d'une ligne (slot + gap)
                const translationY = (currentAttempt - 1) * lineHeight;
                arrow.style.transform = `translateY(-${Math.min(translationY, (totalAttempts - 1) * lineHeight)}px)`;
            }

            // Restaurer les couleurs des slots d'évaluation depuis le localStorage
            let slots = document.querySelectorAll(`.evaluation-area-${currentAttempt} .evaluation-slot`);
            slots.forEach((slot, index) => {
                let savedColor = localStorage.getItem(`evaluation-slot-${currentAttempt}-${index}`);
                if (savedColor) {
                    slot.style.backgroundColor = savedColor;
                }
            });

            // Passer à l'essai suivant après un délai
            currentAttempt++;
            setTimeout(displayNextAttempt, 3000);
        } else {
            console.error("Format incorrect pour l'essai :", attemptStr);
        }
    } else {
        console.log("Fin des tentatives");
    }
}

// Déclencher l'affichage des tentatives après le chargement de la page
window.onload = function () {
    console.log("window.onload appelé");
    if (attempts.length > 0) {
        setTimeout(displayNextAttempt, 1000);
    } else {
        console.warn("Aucune tentative disponible dans attempts.");
    }
};
