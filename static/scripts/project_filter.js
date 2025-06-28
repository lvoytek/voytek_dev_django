document.addEventListener('DOMContentLoaded', function() {
  // Get all checkboxes that start with 'check-'
  const checkboxes = document.querySelectorAll('input[id^="check-"]');

  // Get all project cards
  const projectCards = document.querySelectorAll('.col-3[style*="margin-bottom"]');

  // Check if a project has any of the selected tags or if no tags selected
  function projectHasSelectedTags(projectElement, selectedTags) {
    if (selectedTags.length === 0) return true;

    // Get all tags from the project's chips
    const projectTags = Array.from(projectElement.querySelectorAll('.p-chip__value'))
      .map(tag => tag.textContent.trim());

    // Check if any of the selected tags are present in project tags
    return selectedTags.some(tag => projectTags.includes(tag));
}

  // Update visible projects based on selected tags
  function updateVisibleProjects() {
    // Get all checked checkboxes and extract their tags
    const selectedTags = Array.from(checkboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.id.replace('check-', ''));

    // Show/hide projects based on selected tags
    projectCards.forEach(card => {
      if (projectHasSelectedTags(card, selectedTags)) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  }

  // Add change event listener to all checkboxes
  checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', updateVisibleProjects);
  });
});