var app = new Vue({
    el: '#app',
    data: {
    },
    created: function () {
      
    },
    watch: {},
    methods: {
      modalInit: function (modalBody) {
        document.getElementById('modalBody').innerHTML = modalBody
  
        const elem = document.getElementById('modal1')
        const instance = M.Modal.init(elem, {
          dismissible: true,
          preventScrolling: true,
          startingTop: '4%'
        })
        instance.open()
      },

    },
    computed: {

    },
    updated: function () {},
    mounted () {
    
    }
  })
  