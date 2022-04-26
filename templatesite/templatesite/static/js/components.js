'use strict'

const CLOSE_ACCORDIONS_ONCLICK = true

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

/*
To use this:
Add the [data-accordion-item] HTML attribute around the accordion item.
Then add [data-title] and [data-content] around the title and around the content which will be displayed when the title is clicked.
*/
function watchAccordionItems() {
    const accordionItems = document.querySelectorAll('[data-accordion-item]')
    accordionItems.forEach(item => {
        const title = item.querySelector('[data-title]')
        const content = item.querySelector('[data-content]')

        title.addEventListener('click', () => {
            CLOSE_ACCORDIONS_ONCLICK && closeOtherAccordions(content)

            toggleClass(content, 'display-none')

            const downArrow = item.querySelector('.icon-down-arrow') // todo: use font awesome
            toggleClass(downArrow, 'rotate-180')
        }, { passive: true })
    })
}

function closeOtherAccordions(element) {
    const accordionItems = document.querySelectorAll('[data-accordion-item] [data-content]')
    accordionItems.forEach(item => {
        if (element !== item) {
            item.classList.add('display-none')
        }
    })
}


// ONLOAD
document.addEventListener('DOMContentLoaded', () => {
    watchAccordionItems()
}, false)