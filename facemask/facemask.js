let text = ''
const textToMask = document.querySelector('#faceInput');

const handleInputChange = (e) => {
    text = textToMask.value
    textToMask.value = maskify(text)
}

// Maskify function
const maskify = (text) => {

    if(text.length > 4){
        
        const textToArray = text.split('');
        text = textToArray.map((char, i) => (
          i < text.length - 4 ? '#' : char
        )).join('')
    }
    return text
}