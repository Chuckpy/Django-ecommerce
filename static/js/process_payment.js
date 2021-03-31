var maskCPF = IMask(document.getElementById('docNumber'), {
    mask: '000.000.000-00'
})

var maskCardNumber = IMask(document.getElementById('cardNumber'), {
    mask: '0000000000000000'
})

window.Mercadopago.getIdentificationTypes()

document.getElementById('cardNumber').addEventListener('change', guessPaymentMethod)
function guessPaymentMethod(event) {
    let cardnumber = document.getElementById("cardNumber").value
    if (cardnumber.length >= 6) {
        let bin = cardnumber.substring(0, 6)
        window.Mercadopago.getPaymentMethod({
            "bin": bin
        }, setPaymentMethod)
    }
}

function setPaymentMethod(status, response) {
    if (status == 200) {
        let paymentMethod = response[0]
        document.getElementById('paymentMethodId').value = paymentMethod.id

        getIssuers(paymentMethod.id)
    } else {
        alert(`payment method info error: ${response}`)
    }
}

function getIssuers(paymentMethodId) {
    window.Mercadopago.getIssuers(
        paymentMethodId,
        setIssuers
    )
}

function setIssuers(status, response) {
    if (status == 200) {
        let issuerSelect = document.getElementById('issuer')
        response.forEach(issuer => {
            let opt = document.createElement('option')
            opt.text = issuer.name
            opt.value = issuer.id
            issuerSelect.appendChild(opt)
        })

        getInstallments(
            document.getElementById('paymentMethodId').value,
            document.getElementById('transactionAmount').value,
            issuerSelect.value
        )
    } else {
        alert(`issuers method info error: ${response}`)
    }
}

function getInstallments(paymentMethodId, transactionAmount, issuerId) {
    window.Mercadopago.getInstallments({
        "payment_method_id": paymentMethodId,
        "amount": parseFloat(transactionAmount),
        "issuer_id": parseInt(issuerId)
    }, setInstallments)
}

function setInstallments(status, response) {
    if (status == 200) {
        document.getElementById('installments').options.length = 0
        response[0].payer_costs.forEach(payerCost => {
            let opt = document.createElement('option')
            opt.text = payerCost.recommended_message
            opt.value = payerCost.installments
            document.getElementById('installments').appendChild(opt)
        })
    } else {
        alert(`installments method info error: ${response}`)
    }
}

doSubmit = false
document.getElementById('paymentForm').addEventListener('submit', getCardToken)
function getCardToken(event) {
    event.preventDefault()
    if (!doSubmit) {
        document.getElementById('docNumber').value = maskCPF.unmaskedValue
        let $form = document.getElementById('paymentForm')
        window.Mercadopago.createToken($form, setCardTokenAndPay)
        return false
    }
}

function setCardTokenAndPay(status, response) {
    if (status == 200 || status == 201) {
        let form = document.getElementById('paymentForm')
        let card = document.createElement('input')
        card.setAttribute('name', 'token')
        card.setAttribute('type', 'hidden')
        card.setAttribute('value', response.id)
        form.appendChild(card)
        doSubmit = true
        form.submit()
    } else {
        alert("Verify filled data!\n" + JSON.stringify(response, null, 4))
    }
}