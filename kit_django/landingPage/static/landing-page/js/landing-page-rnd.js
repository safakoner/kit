$(document).ready(function()
{

function getCookie(name)
{
    let cookieValue = null;

    if(document.cookie && document.cookie != '')
    {
        let cookies = document.cookie.split(';');
        for(let i = 0; i < cookies.length; i++)
        {
            let cookie = jQuery.trim(cookies[i]);
            if(cookie.substring(0, name.length + 1) == (name + '='))
            {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function renderContactFormCapthca(elementID, indexList)
{
    let token = getCookie('csrftoken');

    if(token === null)
        return;

    let value = '';

    for(let i=0; i<indexList.length; i++)
        value += token[indexList[i]];

    const canvas  = document.getElementById(elementID);
    const ctx     = canvas.getContext('2d');
    ctx.font      = '1.6em Open Sans';
    ctx.fillStyle = '#515151';

    ctx.fillText(value,6,26);
}

renderContactFormCapthca('contactFormCapthca', [7, 14, 23, 33]);
renderContactFormCapthca('newsletterFormCapthca', [2, 8, 10]);

const anchor = $('site-data').data('anchor');
if(anchor)
    window.location = '#' + anchor;

});