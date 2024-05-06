// Define the URL of the TradeAI Flask API
// New Devika AI API endpoint
const devikaAIUrl = 'https://api.devikaai.com/trading_signals';

function fetchTradingSignals(data) {
    return fetch(devikaAIUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .catch(error => {
        console.error('Error fetching AI-driven trading signals:', error);
        throw error;
    });
}


// Function to execute trades or adjust strategies based on AI feedback
function executeTrade(signal) {
    // Placeholder for trading execution logic, e.g., using TradingView's API
    console.log('Executing trade based on signal:', signal);
    // Actual trading API integration code would go here
}

// Listen for messages from popup.html or content scripts
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === 'fetchSignals') {
        fetchTradingSignals(request.data)
            .then(signals => {
                console.log('Received trading signals:', signals);
                // Process each trading signal
                signals.forEach(signal => {
                    executeTrade(signal);
                });
                sendResponse({status: 'success', signals: signals});
            })
            .catch(error => {
                console.error('Failed to process trading signals:', error);
                sendResponse({status: 'error', message: error.message});
            });
        return true; // Indicates that the response is asynchronous
    }
});

console.log('Background script for TradeAI Extension loaded and running.');