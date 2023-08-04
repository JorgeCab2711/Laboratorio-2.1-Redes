

















// Translator part

function stringToBinary(input) {
    return input.split('').map(function(char) {
        return char.charCodeAt(0).toString(2).padStart(8, '0');
    }).join(' ');
}

function binaryToString(binary) {
    return binary.split(' ').map(function(bin) {
        return String.fromCharCode(parseInt(bin, 2));
    }).join('');
}

