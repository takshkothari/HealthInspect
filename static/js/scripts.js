const path="";
function readURL(input) {
    if (input.files && input.files[0]) {                      
      var inputFileData = input.files[0];                     
      var reader = new FileReader();                          
      reader.onload = function(e) {                           
        console.log('e',e) 
        $('.file-upload-placeholder').hide();                 
        $('.file-upload-image').attr('src', e.target.result); 
        $('.file-upload-preview').show();                     
        $('.image-title').html(inputFileData.name);           
      };
      console.log('input.files[0]',input.files[0])
      reader.readAsDataURL(inputFileData);     
    } else { removeUpload(); }
  }
  
  function removeUpload() {
    var $clone = $('.file-upload-input').val('').clone(true); 
    $('.file-upload-input').replaceWith($clone);              
    $('.file-upload-placeholder').show();                     
    $('.file-upload-preview').hide();                         
  }
  
  $('.file-upload-placeholder').bind('dragover', function () {
    $('.file-upload-placeholder').addClass('image-dropping');
  });
  $('.file-upload-placeholder').bind('dragleave', function () {
    $('.file-upload-placeholder').removeClass('image-dropping');
  });