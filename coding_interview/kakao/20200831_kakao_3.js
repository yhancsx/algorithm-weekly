// Syntax : ES6

const removeAllModal = () => document.querySelectorAll('.cover').forEach(element => element.remove())
const onClickDeleteOK = () => new Modal('삭제되었습니다.', [['확인', 'btn_delete', removeAllModal]])

const onClickDelete = (e) => {
    e.target.blur();
    const targetValue = e.target.value;
    const deleteArticle = () => {
        document.querySelector(`#article_${targetValue}`).remove()
        onClickDeleteOK()
    }
    const modal = new Modal('삭제하시겠습니까', [['확인', 'btn_delete', deleteArticle],['취소', 'btn_delete', undefined]])
}
Array.from(document.getElementsByClassName('btn_delete')).map(element => element.addEventListener('click', onClickDelete))

function Modal(content="삭제하시겠습니까??", buttons=[['취소', 'btn_delete', undefined]] ) {
    const modalCover = document.createElement('div');
    modalCover.className = 'cover';

    const modalDimmed = document.createElement('div');
    modalDimmed.className = 'dimmed';

    const modalWrapper = document.createElement('div');
    modalWrapper.className = 'wrapper';

    const modalContainer = document.createElement('div');
    modalContainer.className = 'modal';

    const modalContent = document.createElement('p');
    modalContent.className = 'content';
    modalContent.textContent = content;

    const modalFooter = document.createElement('footer');

    buttons.forEach(([buttonContent, buttonClass, onClick]) => {
        const button = document.createElement('button');
        button.textContent = buttonContent;
        button.className = buttonClass;
        button.focus();
        modalFooter.appendChild(button)

        const onClickButton = (e) => {
            e.target.blur();
            try {
                onClick === undefined? modalCover.remove() : onClick(e);
            }catch {
                new Modal('작업에 실패하였습니다..', [['확인', 'btn_delete', removeAllModal]])
            }

        }
        button.addEventListener('click', onClickButton);
    })

    modalContainer.appendChild(modalContent);
    modalContainer.appendChild(modalFooter);
    modalWrapper.appendChild(modalContainer);
    modalCover.appendChild(modalDimmed);
    modalCover.appendChild(modalWrapper);
    document.querySelector('body').appendChild(modalCover)
    document.querySelector('body').classList.add('modal-open')
}