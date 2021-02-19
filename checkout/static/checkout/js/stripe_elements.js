
var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1)
var clientSecret = $('#client_secret').text().slice(1, -1)

var stripe = Stripe(stripePublicKey);

var elements = stripe.elements();
var style = {
  base: {
    color: "#32325d",
      fontFamily: '"Josefin Slab", Arial, sans-serif',
      fontSmoothing: "antialiased",
      fontSize: "16px",
      "::placeholder": {
        color: "#aab7c4"
      }
    },
    invalid: {
      color: "#ff0000" ,
      iconColor: "#ff0000"
  }
};

// Realtime validations
var card = elements.create("card", { style: style });
card.mount("#card-element");

card.addEventListener('change', function(event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
      var html = `
            <span role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(displayError).html(html);
  } else {
    displayError.textContent = '';
  }
});

// Form Submit
var form = document.getElementById('payment-info-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();
    card.update({ 'disabled': true });
    $('#pay-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            var displayError = document.getElementById('card-errors');
            var html = `
                <span role="alert">
                <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(displayError).html(html);
            card.update({ 'disabled': false });
            $('#pay-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});
