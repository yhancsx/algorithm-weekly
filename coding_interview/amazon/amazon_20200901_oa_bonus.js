// IMPORT LIBRARY PACKAGES NEEDED BY YOUR PROGRAM
// SOME FUNCTIONALITY WITHIN A PACKAGE MAY BE RESTRICTED
// DEFINE ANY FUNCTION NEEDED
// FUNCTION SIGNATURE BEGINS, THIS FUNCTION IS REQUIRED
function retrieveMostFrequentlyUsedWords(literatureText, wordsToExclude)
{
    // WRITE YOUR CODE HERE
    const words = literatureText.toLowerCase().split(/[\W\d]+/)
    const excludes = new Set(wordsToExclude)
    const wordCount = {}
    
    words.forEach(word => {
        if (excludes.has(word) || word ==='') return;
        if (word in wordCount) wordCount[word] +=1;
        else wordCount[word] = 1;
    })

    let max = -1;
    let answer = [];
    for(const [word, count] of Object.entries(wordCount)) {
        if (count > max) {
            answer = [word]
            max = count
        }
        else if (count === max) answer.push(word)
        
    }
    return answer
}
// FUNCTION SIGNATURE ENDS