const botoesNumericos = document.querySelectorAll('.botaoNumerico');
const botoesOperacao = document.querySelectorAll('.botaoOperacao');
const botaoIgual = document.querySelector('.botaoIgual');

const visorCima = document.querySelector('.operacaoPassada');
const visorBaixo = document.querySelector('.operacaoAtual');

function igual(){
    visorCima.innerHTML += " " + visorBaixo.innerHTML;
    visorBaixo.innerHTML = "tem que ver com o backend"
}
botaoIgual.addEventListener('click', function(){
    igual()
});

botoesNumericos.forEach(botao => {
  botao.addEventListener('click', function() {
      if (botao.value === '+/-'){
          if(visorBaixo.innerHTML[0] === '-'){
              visorBaixo.innerHTML = visorBaixo.innerHTML.slice(1);
              return
          }
          visorBaixo.innerHTML = '-' + visorBaixo.innerHTML
          return
        }
      visorBaixo.innerHTML += botao.value;

  });
});
botoesOperacao.forEach(botao => {
    botao.addEventListener('click', function() {
        if (botao.value == 'backspace'){
            visorBaixo.innerHTML = visorBaixo.innerHTML.slice(0, -1);
        }
        if (botao.value === '/'){
            if (visorCima.innerHTML != ''){
                igual()
                return
            }
            visorCima.innerHTML = visorBaixo.innerHTML + ' ÷';
            visorBaixo.innerHTML = '';
        }
        if (botao.value === '*'){
            if (visorCima.innerHTML != ''){
                igual()
                return
            }
            visorCima.innerHTML = visorBaixo.innerHTML + ' ×';
            visorBaixo.innerHTML = '';
        }
        if (botao.value === '+'){
            if (visorCima.innerHTML != ''){
                igual()
                return
            }
            visorCima.innerHTML = visorBaixo.innerHTML + ' +';
            visorBaixo.innerHTML = '';
        }
        if (botao.value === '-'){
            if (visorCima.innerHTML != ''){
                igual()
                return
            }
            visorCima.innerHTML = visorBaixo.innerHTML + ' -';
            visorBaixo.innerHTML = '';
        }
        if (botao.value === 'CE'){
            visorBaixo.innerHTML = '';
        }
        if (botao.value === 'C'){
            visorBaixo.innerHTML = '';
            visorCima.innerHTML = '';
        }
        if (botao.value === '%'){
            if (visorBaixo.innerHTML == ''){
                visorBaixo.innerHTML = '0';
            }
            visorBaixo.innerHTML += '%';
            igual()
        }
        if (botao.value === '1/x'){
            if (visorBaixo.innerHTML == ''){
                visorBaixo.innerHTML = '1/'+visorCima.innerHTML.slice(0, -2);
                return
            }
            visorBaixo.innerHTML = '1/'+visorCima.innerHTML;
            igual()
        }
        if (botao.value === 'sqrt'){
            if (visorBaixo.innerHTML == ''){
                visorBaixo.innerHTML = 'sqrt(' + visorCima.innerHTML + ')';
                return
            }
            visorBaixo.innerHTML = 'sqrt(' + visorBaixo.innerHTML + ')';
            igual()
        }
        if (botao.value === 'x^2'){
            if (visorBaixo.innerHTML == ''){
                visorBaixo.innerHTML = visorCima.innerHTML.slice(0, -2) + '^2';
                return
            }
            visorBaixo.innerHTML += visorCima.innerHTML+'^2';
            igual()
        }



    })
})