import React, {useState} from 'react';
import classnames from 'classnames';
// you should import `lodash` as a whole module
import lodash from 'lodash';
import axios from 'axios';

const ITEMS_API_URL = 'https://example.com/api/items';
const DEBOUNCE_DELAY = 500;

// the exported component can be either a function or a class

const fetchItems = async (query) => {
  const response = await axios.get(`${ITEMS_API_URL}?q=${query}`);
  return response.data
};

export default function Autocomplete({onSelectItem}) {
  const [itemList, setItemList] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const onInputChange = lodash.debounce(async (e) => {
    e.preventDefault();
    const value = document.getElementsByClassName('input')[0].value;
    // const value = e.target.value;

    setIsLoading(true);
    const list = await fetchItems(value);
    setItemList(list);
    setIsLoading(false);

  }, DEBOUNCE_DELAY);

  return (
      <div className="wrapper">
        <div className={classnames('control', {'is-loading': isLoading})}>
          <input type="text" className="input" onChange={e=>onInputChange(e)}/>
        </div>
        {!isLoading && itemList.length>0 && <div className="list is-hoverable" >
          {itemList.map(item => (
              <a className='list-item' onClick={()=>onSelectItem(item)}>
                {item}
              </a>
          ))}
        </div>}
      </div>
  );
}
