// inline_script_usage.js

// Import the generateNonce function from the runtime_nonce_generator.js file
import { generateNonce } from './runtime_nonce_generator.js';

// Function to add a secure inline script to the document
function addSecureInlineScript() {
    // Generate a nonce
    const nonce = generateNonce();

    // Create a new script element
    const script = document.createElement('script');

    // Set the nonce attribute with the generated nonce
    script.setAttribute('nonce', nonce);

    // Define the secure inline script content
    const scriptContent = `
        console.log('This is a secure inline script with nonce:', '${nonce}');
    `;

    // Add the script content to the script element
    script.textContent = scriptContent;

    // Append the script element to the document's head
    document.head.appendChild(script);
}

// Call the function to add the script to the document
addSecureInlineScript();