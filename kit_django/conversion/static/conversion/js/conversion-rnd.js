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


function getCapthca()
{
    let token = getCookie('csrftoken');

    if(token === null)
        return;

    const indexList =  [7, 14, 23, 33];

    let value = "";
    for(let i=0; i<indexList.length; i++)
        value += token[indexList[i]];

    const canvas  = document.getElementById('capthca');
    const ctx     = canvas.getContext('2d');
    ctx.font      = '1.2em Open Sans';
    ctx.fillStyle = 'rgb(36, 36, 36)';
    ctx.fillText(value,14,25);
}
getCapthca();

});