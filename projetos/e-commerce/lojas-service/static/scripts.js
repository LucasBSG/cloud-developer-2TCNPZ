document.getElementById('cadastro-loja-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const nome = document.getElementById('nome').value;
    const descricao = document.getElementById('descricao').value;
    const endereco = document.getElementById('endereco').value;
    const contato = document.getElementById('contato').value;

    fetch('/lojas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `nome=${nome}&descricao=${descricao}&endereco=${endereco}&contato=${contato}`
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadLojas();
    });
});

document.getElementById('associar-produto-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const lojaId = document.getElementById('loja-id').value;
    const produtoId = document.getElementById('produto-id').value;

    fetch('/produtos_lojas', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: `loja_id=${lojaId}&produto_id=${produtoId}`
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    });
});

document.getElementById('dashboard-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const lojaId = document.getElementById('dashboard-loja-id').value;

    fetch(`/dashboard/${lojaId}`)
    .then(response => response.json())
    .then(data => {
        const dashboardDiv = document.getElementById('dashboard');
        dashboardDiv.innerHTML = `<h3>Vendas</h3><pre>${JSON.stringify(data.vendas, null, 2)}</pre>
                                  <h3>Estoque</h3><pre>${JSON.stringify(data.estoque, null, 2)}</pre>`;
    });
});

function loadLojas() {
    fetch('/lojas')
    .then(response => response.json())
    .then(data => {
        const lojasList = document.getElementById('lojas-list');
        lojasList.innerHTML = '<h3>Lojas Cadastradas</h3><ul>' + data.lojas.map(loja => `<li>${loja.nome} - ${loja.descricao}</li>`).join('') + '</ul>';
    });
}

loadLojas();