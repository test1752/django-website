document.addEventListener('DOMContentLoaded', function() {
    const contentCheckbox = document.querySelector('#id_content');
    const descriptionField = document.querySelector('.field-description');

    function toggleDescriptionField() {
        if (contentCheckbox.checked) {
            descriptionField.style.display = 'block';
        } else {
            descriptionField.style.display = 'none';
        }
    }

    toggleDescriptionField();

    // event listener on checkbox
    contentCheckbox.addEventListener('change', toggleDescriptionField);
});