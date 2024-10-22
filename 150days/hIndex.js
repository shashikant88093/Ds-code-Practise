// Input: citations = [3,0,6,1,5]
// Output: 3
// Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
// Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.


function calculateHIndex(citations) {
    // Sort citations in descending order
    citations.sort((a, b) => b - a);
    let hIndex = 0;
    for (let i = 0; i < citations.length; i++) {
        // If the current citation count is greater than or equal to the number of papers
        if (citations[i] >= i + 1) {
            hIndex = i + 1; // Update h-index
        } else {
            break; // No need to check further, as citations are sorted
        }
    }
    return hIndex;
}

// Example input
const citations = [3, 0, 6, 1, 5];
const hIndex = calculateHIndex(citations);
console.log(hIndex); // Output: 3
