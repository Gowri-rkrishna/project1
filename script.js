// Function to fetch best plans based on data usage and plan duration
async function fetchBestPlans(dataUsage, planDuration) {
    const apiUrl = `http://127.0.0.1:5000/api/best_plans?data_usage=${dataUsage}&plan_duration=${planDuration}`;

    try {
        const response = await fetch(apiUrl);

        // Check if the response is ok (status code 200-299)
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        // Parse the JSON response
        const bestPlans = await response.json();
        console.log('Best Plans:', bestPlans);
    } catch (error) {
        console.error('Error fetching best plans:', error);
    }
}

// Example usage
const dataUsage = 10; // Example data usage in GB
const planDuration = '30 days'; // Example plan duration
fetchBestPlans(dataUsage, planDuration);