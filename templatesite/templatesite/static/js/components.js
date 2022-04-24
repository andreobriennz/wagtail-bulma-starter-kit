'use strict'

// UTILS
function el(selector) {
    return document.querySelector(selector)
}

function toggleClass(element, className) {
    element.classList.toggle(className)
}

function toggleAriaExpanded(element) {
    const currentValue = element.getAttribute('aria-expanded')
    const newValue = currentValue === 'true' ? 'false' : 'true'
    element.setAttribute('aria-expanded', newValue)
}

// only if not using `display: none;`
function toggleTabindex(element) {
    if (element.tabIndex === 0) {
        element.tabIndex = -1
    } else {
        element.tabIndex = 0
    }
}

// COMPONENTS
window.toggleNav = () => {
    const hamburgerIcon = el('#nav-hamburger')
    const navMenu = el('#mobile-nav')

    toggleClass(hamburgerIcon, 'is-active')
    toggleClass(navMenu, 'is-active')
    toggleAriaExpanded(hamburgerIcon)
}

window.handleSearch = function(selector) {
    const query = document.querySelector(selector).value
    window.location.href = '/search?query=' + query
    return false
}

document.addEventListener('DOMContentLoaded', () => {
    // watchAccordionItems()
}, false)