document.addEventListener('DOMContentLoaded', function() {
    // Attach event listener to #fetchSignals button
    var fetchSignalsButton = document.getElementById('fetchSignals');
    fetchSignalsButton.addEventListener('click', function() {
        fetchSignals();
    });

    // Attach event listener to #executeTrades button
    var executeTradesButton = document.getElementById('executeTrades');
    executeTradesButton.addEventListener('click', function() {
        executeTrades();
    });
});

// Function to fetch signals from Codellama on Ollama locally
function fetchSignals() {
    console.log("Fetching trading signals from Codellama on Ollama...");

    // Assuming Codellama on Ollama has an endpoint to fetch trading signals locally
    const codellamaUrl = 'http://localhost:5000/trading_signals'; // Adjust port if necessary

    // Placeholder data to fetch signals; replace with actual data as needed
    const requestData = { parameter: 'value' };

    fetch(codellamaUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestData)
    })
    .then(response => response.json())
    .then(signals => {
        console.log("Received signals:", signals);
        document.getElementById('signalsContent').textContent = JSON.stringify(signals, null, 2);
    })
    .catch(error => {
        console.error('Error fetching trading signals:', error);
        document.getElementById('statusContent').textContent = 'Error: ' + error.message;
    });
}

// Function to execute trades based on Codellama on Ollama locally
function executeTrades() {
    console.log("Executing trades based on trading signals from Codellama on Ollama...");

    // Assuming Codellama on Ollama provides an endpoint for trade execution locally
    const tradeExecutionUrl = 'http://localhost:5000/execute_trades'; // Adjust port if necessary

    // Placeholder data for executing trades; replace with actual signal data
    const tradeData = { tradeDetails: 'trade-parameters' };

    fetch(tradeExecutionUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(tradeData)
    })
    .then(response => response.json())
    .then(result => {
        console.log("Trade execution response:", result);
        document.getElementById('statusContent').textContent = 'Trade executed successfully: ' + JSON.stringify(result);
    })
    .catch(error => {
        console.error('Error executing trades:', error);
        document.getElementById('statusContent').textContent = 'Error executing trades: ' + error.message;
    });
}
