function DisplayPoem(info) {
    var poem = + info + "had a little" + info + "little" + info + "little" + info + + info + "had a little" + info +, "it`s fleece was" + info + "as snow. It followed her to" + info + "one day," + info + "one day," + info + "one day, it made the children" + info + "and play to see a" + info + "at" + info +;
    $('#output').html(poem);
}

$('#submitName').click(function(){
    var passThis = $('input[name="studentName"]').val();
    DisplayPoem(passThis);
});
