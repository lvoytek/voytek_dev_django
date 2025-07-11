// Open or close the nav dropdown on smaller screens
function toggleDropdown(toggle, open) {
  var parentElement = toggle.parentNode;
  var dropdown = document.getElementById(toggle.getAttribute('aria-controls'));
  dropdown.setAttribute('aria-hidden', !open);

  if (open) {
    parentElement.classList.add('is-active');
  } else {
    parentElement.classList.remove('is-active');
  }
}

// Close all dropdown menus
function closeAllDropdowns(toggles) {
  toggles.forEach(function(toggle) {
    toggleDropdown(toggle, false);
  });
}

// Close dropdown menu when clicking outside of it
function handleClickOutside(toggles, containerClass) {
  document.addEventListener('click', function(event) {
    var target = event.target;

    if (target.closest) {
      if (!target.closest(containerClass)) {
        closeAllDropdowns(toggles);
      }
    }
  });
}

// Nav menu dropdown initialization
function initNavDropdowns(containerClass) {
  var toggles = [].slice.call(document.querySelectorAll(containerClass + ' [aria-controls]'));

  handleClickOutside(toggles, containerClass);

  toggles.forEach(function(toggle) {
    toggle.addEventListener('click', function(e) {
      e.preventDefault();

      const shouldOpen = !toggle.parentNode.classList.contains('is-active');
      closeAllDropdowns(toggles);
      toggleDropdown(toggle, shouldOpen);
    });
  });
}

initNavDropdowns('.p-navigation__item--dropdown-toggle')