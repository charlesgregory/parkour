Ext.define('MainHub.store.NavigationTree', {
    extend: 'Ext.data.TreeStore',

    storeId: 'NavigationTree',

    fields: [{
        name: 'text'
    }],

    root: {
        expanded: true,
        children: [
            // {
            //     text: 'Start Page',
            //     iconCls: 'x-fa fa-th-large',
            //     viewType: 'startpage',
            //     leaf: true
            // },
            // {
            //     text: 'Dashboard',
            //     iconCls: 'x-fa fa-desktop',
            //     viewType: 'dashboard',
            //     // routeId: 'dashboard', // routeId defaults to viewType
            //     leaf: true
            // },
            {
                text: 'Tables',
                iconCls: 'x-fa fa-table',
                expanded: true,
                selectable: false,
                children: [
                    {
                        text: 'Researchers',
                        iconCls: 'x-fa fa-user',
                        viewType: 'researchers',
                        leaf: true
                    },
                    {
                        text: 'Requests',
                        iconCls: 'x-fa fa-external-link-square',
                        viewType: 'requests',
                        leaf: true
                    },
                    {
                        text: 'Libraries/Samples',
                        iconCls: 'x-fa fa-flask',
                        viewType: 'libraries',
                        leaf: true
                    }
                ]
            },
            {
                text: 'Quality Control',
                iconCls: 'x-fa fa-check-square',
                expanded: true,
                selectable: false,
                children: [
                    {
                        text: 'Incoming Libraries/Samples',
                        iconCls: 'x-fa fa-check',
                        viewType: 'incoming-libraries',
                        leaf: true
                    }
                ]
            }
        ]
    }
});
