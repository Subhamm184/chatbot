document.addEventListener("DOMContentLoaded", () => {
    const startQuizButton = document.getElementById("startQuiz");
    const quizContainer = document.getElementById("quizContainer");
    const resultContainer = document.getElementById("resultContainer");
    const questionsDiv = document.getElementById("questions");
    const applyNowButton = document.getElementById("applyNow");

    let currentQuestionIndex = 0;
    let questions = [];
    let answers = [];

    // Event listener for starting the quiz
    startQuizButton.addEventListener("click", async () => {
        const company = document.getElementById("company").value;
        const profession = document.querySelector('input[name="profession"]:checked')?.value;
        const skills = document.getElementById("skills").value;

        if (!company || !profession || !skills) {
            alert("Please fill all fields before starting the quiz.");
            return;
        }

        // Fetch questions from the server
        try {
            const response = await fetch("/start_quiz", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ company, profession, skills })
            });

            const data = await response.json();

            if (response.ok) {
                questions = data.questions;
                currentQuestionIndex = 0;
                answers = Array(questions.length).fill(""); // Initialize empty answers array
                showQuestion(currentQuestionIndex);
                quizContainer.classList.remove("hidden");
            } else {
                alert(data.error || "Failed to fetch questions.");
            }
        } catch (error) {
            console.error("Error starting quiz:", error);
            alert("An error occurred while starting the quiz. Please try again.");
        }
    });

    // Function to show a question based on the current index
    function showQuestion(index) {
        if (index < questions.length) {
            questionsDiv.innerHTML = `
                <div class="question">
                    <p>${questions[index]}</p>
                    <label>
                        <input type="radio" name="answer" value="yes"> Yes
                    </label>
                    <label>
                        <input type="radio" name="answer" value="no"> No
                    </label>
                </div>
                <div class="navigation">
                    ${index > 0 ? '<button id="prevQuestion">Previous</button>' : ""}
                    ${index < questions.length - 1 ? '<button id="nextQuestion">Next</button>' : '<button id="submitQuiz">Submit</button>'}
                </div>
            `;

            // Event listeners for navigation buttons
            document.getElementById("nextQuestion")?.addEventListener("click", () => {
                saveAnswer(index);
                currentQuestionIndex++;
                showQuestion(currentQuestionIndex);
            });

            document.getElementById("prevQuestion")?.addEventListener("click", () => {
                saveAnswer(index);
                currentQuestionIndex--;
                showQuestion(currentQuestionIndex);
            });

            document.getElementById("submitQuiz")?.addEventListener("click", () => {
                saveAnswer(index);
                submitQuiz();
            });
        }
    }

    // Function to save the answer for the current question
    function saveAnswer(index) {
        const selectedAnswer = document.querySelector('input[name="answer"]:checked')?.value;
        if (selectedAnswer) {
            answers[index] = selectedAnswer;
        }
    }

    // Function to submit the quiz and display the result
    async function submitQuiz() {
        try {
            const response = await fetch("/submit_quiz", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ answers })
            });

            const data = await response.json();

            if (response.ok) {
                quizContainer.classList.add("hidden");
                resultContainer.classList.remove("hidden");
                document.getElementById("resultMessage").textContent = `${data.eligibility} Your score: ${data.score}%.`;
                if (data.score >= 70) {
                    applyNowButton.classList.remove("hidden");
                }
            } else {
                alert(data.error || "Failed to submit quiz.");
            }
        } catch (error) {
            console.error("Error submitting quiz:", error);
            alert("An error occurred while submitting the quiz. Please try again.");
        }
    }
});
