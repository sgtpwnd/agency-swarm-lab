// runtime_nonce_generator.js

// Function to generate a nonce using the Web Crypto API
function generateNonce() {
    const array = new Uint8Array(16); // Generate 16 random bytes
    crypto.getRandomValues(array); // Fill the array with random values
    // Convert the byte array to a hexadecimal string
    return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
}

// Export the generateNonce function to be used in other scripts
export { generateNonce };