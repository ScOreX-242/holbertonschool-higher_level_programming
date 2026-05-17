document.querySelector('#add_item').onclick = function () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('.my_list').appendChild(li);
};
