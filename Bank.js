// filepath: c:\Users\USER\Desktop\Jesujoba html\PRACTICE HTML\bank-app\js\bank.js
// ...existing code...
(function(){
  const LS_KEY = 'simpleBankApp.v1';
  const form = document.getElementById('entry-form');
  const desc = document.getElementById('desc');
  const amount = document.getElementById('amount');
  const typeEl = document.getElementById('type');
  const dateEl = document.getElementById('date');
  const transactionsEl = document.getElementById('transactions');
  const balanceEl = document.getElementById('balance');
  const incomeEl = document.getElementById('total-income');
  const expenseEl = document.getElementById('total-expense');
  const emptyEl = document.getElementById('empty');
  const filters = document.querySelectorAll('[data-filter]');
  const search = document.getElementById('search');
  const clearAllBtn = document.getElementById('clear-all');
  const quickIncome = document.getElementById('quick-income');
  const quickExpense = document.getElementById('quick-expense');

  let data = JSON.parse(localStorage.getItem(LS_KEY) || '[]');
  let filter = 'all';
  let query = '';

  function save(){
    localStorage.setItem(LS_KEY, JSON.stringify(data));
  }

  function formatCurrency(n){
    return new Intl.NumberFormat(undefined, {style:'currency',currency:'USD',minimumFractionDigits:2}).format(n);
  }

  function totals(list){
    const income = list.filter(i=>i.amount>0).reduce((s,i)=>s+i.amount,0);
    const expense = list.filter(i=>i.amount<0).reduce((s,i)=>s+i.amount,0);
    const bal = income + expense;
    return {income, expense: Math.abs(expense), bal};
  }

  function render(){
    const visible = data
      .filter(t=>{
        if (filter === 'income') return t.amount>0;
        if (filter === 'expense') return t.amount<0;
        return true;
      })
      .filter(t => t.description.toLowerCase().includes(query.toLowerCase()));
    transactionsEl.innerHTML = '';
    if (visible.length === 0) emptyEl.style.display = '';
    else emptyEl.style.display = 'none';

    visible.sort((a,b)=> new Date(b.date||0) - new Date(a.date||0) || b.id - a.id);

    for (const tx of visible){
      const item = document.createElement('div');
      item.className = 'item';
      const meta = document.createElement('div');
      meta.className = 'meta';
      const title = document.createElement('div');
      title.textContent = tx.description || '(no description)';
      const small = document.createElement('small');
      small.textContent = (tx.date ? new Date(tx.date).toLocaleDateString() + ' • ' : '') + tx.category || '';
      small.style.color = 'var(--muted)';
      meta.appendChild(title);
      meta.appendChild(small);

      const right = document.createElement('div');
      right.style.display = 'flex';
      right.style.alignItems = 'center';
      right.style.gap = '8px';

      const am = document.createElement('div');
      am.className = 'amount ' + (tx.amount>0 ? 'in' : 'out');
      am.textContent = (tx.amount>0 ? '+' : '-') + formatCurrency(Math.abs(tx.amount));
      right.appendChild(am);

      const actions = document.createElement('div');
      actions.className = 'actions';
      const del = document.createElement('button');
      del.title = 'Delete';
      del.innerHTML = '🗑';
      del.addEventListener('click', ()=> {
        data = data.filter(d=>d.id!==tx.id);
        save(); render(); updateSummary();
      });
      actions.appendChild(del);

      const edit = document.createElement('button');
      edit.title = 'Edit';
      edit.innerHTML = '✏️';
      edit.addEventListener('click', () => {
        desc.value = tx.description;
        amount.value = Math.abs(tx.amount);
        typeEl.value = tx.amount>0 ? 'income':'expense';
        dateEl.value = tx.date || '';
        editId = tx.id;
      });
      actions.appendChild(edit);

      right.appendChild(actions);

      item.appendChild(meta);
      item.appendChild(right);
      transactionsEl.appendChild(item);
    }
  }

  let editId = null;
  function updateSummary(){
    const {income, expense, bal} = totals(data);
    balanceEl.textContent = formatCurrency(bal);
    incomeEl.textContent = '+' + formatCurrency(income);
    expenseEl.textContent = '-' + formatCurrency(expense);
  }

  form.addEventListener('submit', e=>{
    e.preventDefault();
    const d = desc.value.trim();
    let a = parseFloat(amount.value);
    if (!d || isNaN(a) || a === 0) return alert('Enter valid description and amount');
    const t = typeEl.value;
    if (t === 'expense') a = -Math.abs(a);
    else a = Math.abs(a);
    const date = dateEl.value || new Date().toISOString().slice(0,10);
    if (editId){
      data = data.map(item => item.id === editId ? {...item, description:d, amount:a, date, category: t} : item);
      editId = null;
    } else {
      data.push({ id: Date.now() + Math.floor(Math.random()*1000), description: d, amount: a, date, category: t });
    }
    save();
    form.reset();
    render();
    updateSummary();
  });

  filters.forEach(btn=>{
    btn.addEventListener('click', ()=>{
      filters.forEach(b=>b.style.borderColor='rgba(255,255,255,0.03)');
      btn.style.borderColor = 'white';
      filter = btn.dataset.filter;
      render();
    });
  });

  search.addEventListener('input', (e)=>{ query = e.target.value; render(); });

  clearAllBtn.addEventListener('click', ()=>{
    if (!confirm('Clear ALL transactions?')) return;
    data = [];
    save();
    render();
    updateSummary();
  });

  quickIncome.addEventListener('click', ()=>{
    data.push({ id: Date.now()+Math.random(), description:'Quick Income', amount:50, date:new Date().toISOString().slice(0,10), category:'income' });
    save(); render(); updateSummary();
  });
  quickExpense.addEventListener('click', ()=>{
    data.push({ id: Date.now()+Math.random(), description:'Quick Expense', amount:-20, date:new Date().toISOString().slice(0,10), category:'expense' });
    save(); render(); updateSummary();
  });

  // init
  render();
  updateSummary();
})();